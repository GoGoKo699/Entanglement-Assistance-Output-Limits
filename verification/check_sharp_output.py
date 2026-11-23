"""Check small Clifford examples and entropy bounds used in sharp_examples.md.

The uniform upper and lower dimension laws follow from the analytic proofs.
"""

from itertools import product

import numpy as np


def tensor_product(operators):
    result = np.eye(1)
    for operator in operators:
        result = np.kron(result, operator)
    return result


def clifford_generators(count):
    identity = np.eye(2)
    pauli_x = np.array([[0, 1], [1, 0]])
    pauli_y = np.array([[0, -1j], [1j, 0]])
    pauli_z = np.diag([1, -1])
    qubits = (count + 1) // 2
    generators = [
        tensor_product([pauli_z] * site + [axis] + [identity] * (qubits - site - 1))
        for site, axis in product(range(qubits), (pauli_x, pauli_y))
    ]
    return generators[:count]


def traceless_basis(dimension, commuting):
    basis = []
    if not commuting:
        for row in range(dimension):
            for column in range(row + 1, dimension):
                matrix_unit = np.zeros((dimension, dimension))
                matrix_unit[row, column] = 1
                basis.extend(
                    (
                        (matrix_unit + matrix_unit.T) / np.sqrt(2),
                        1j * (matrix_unit - matrix_unit.T) / np.sqrt(2),
                    )
                )
    for index in range(1, dimension):
        diagonal = np.array([1] * index + [-index] + [0] * (dimension - index - 1))
        basis.append(np.diag(diagonal) / np.sqrt(index * (index + 1)))
    return basis


def relative_entropy_to_uniform(state):
    eigenvalues = np.linalg.eigvalsh(state)
    deviations = len(eigenvalues) * eigenvalues - 1
    return np.mean((1 + deviations) * np.log1p(deviations) - deviations)


def entropy(state):
    eigenvalues = np.linalg.eigvalsh(state)
    eigenvalues = eigenvalues[eigenvalues > 0]
    return -np.sum(eigenvalues * np.log(eigenvalues))


def check_schmidt_inputs(generators, output_basis, t, alpha):
    dimension = output_basis[0].shape[0]
    input_dimension = generators[0].shape[0]
    rng = np.random.default_rng(20261123)
    for rank in (1, min(3, input_dimension), input_dimension):
        matrix = rng.normal(size=(input_dimension, rank)) + 1j * rng.normal(
            size=(input_dimension, rank)
        )
        vectors, _ = np.linalg.qr(matrix)
        weights = np.geomspace(0.001, 1, rank)
        weights /= np.sum(weights)
        root_weights = np.diag(np.sqrt(weights))
        reference = np.diag(weights)
        base = np.kron(reference, np.eye(dimension) / dimension)
        compressed_sum = sum(
            np.kron((vectors.conj().T @ generator @ vectors).T, basis)
            for generator, basis in zip(generators, output_basis)
        )
        root_reference = np.kron(root_weights, np.eye(dimension))
        perturbation = t * root_reference @ compressed_sum @ root_reference
        joint_state = base + perturbation
        result = joint_state.reshape(rank, dimension, rank, dimension)
        output_state = np.trace(result, axis1=0, axis2=2)
        information = entropy(reference) + entropy(output_state) - entropy(joint_state)
        np.testing.assert_allclose(np.trace(joint_state), 1.0, atol=1e-12)
        assert np.linalg.eigvalsh(perturbation + alpha * base)[0] >= -1e-12
        assert np.linalg.eigvalsh(alpha * base - perturbation)[0] >= -1e-12
        upper = dimension * len(generators) * t**2 / (2 * (1 - alpha))
        assert -1e-12 <= information <= upper + 1e-12


def check_example(dimension, commuting):
    basis = traceless_basis(dimension, commuting)
    count = len(basis)
    generators = clifford_generators(count)
    input_dimension = generators[0].shape[0]
    input_identity = np.eye(input_dimension)
    uniform_output = np.eye(dimension) / dimension
    np.testing.assert_allclose([np.trace(matrix) for matrix in generators], 0)
    np.testing.assert_allclose([np.trace(matrix) for matrix in basis], 0, atol=1e-12)
    for row, column in product(range(count), repeat=2):
        first, second = generators[row], generators[column]
        np.testing.assert_allclose(
            first @ second + second @ first, 2 * (row == column) * input_identity
        )
        np.testing.assert_allclose(
            np.trace(basis[row] @ basis[column]).real, float(row == column), atol=1e-12
        )

    operator_sum = sum(
        np.kron(gamma.T, direction) for gamma, direction in zip(generators, basis)
    )
    joint_dimension = input_dimension * dimension
    uniform_joint = np.eye(joint_dimension) / joint_dimension
    for alpha in (0.5, 0.05, 0.001):
        t = alpha / (dimension * count)
        choi = uniform_joint + t * operator_sum / input_dimension
        measure_prepare_choi = sum(
            np.kron(
                (input_identity + sign * gamma).T / (2 * count),
                uniform_output + sign * count * t * direction,
            )
            for gamma, direction in zip(generators, basis)
            for sign in (-1, 1)
        ) / input_dimension
        np.testing.assert_allclose(choi, measure_prepare_choi, atol=1e-12)
        for direction, sign in product(basis, (-1, 1)):
            prepared = uniform_output + sign * count * t * direction
            minimum = np.linalg.eigvalsh(prepared)[0]
            assert minimum >= (1 - alpha) / dimension - 1e-12
        pair_information = sum(
            relative_entropy_to_uniform(uniform_output + sign * t * basis[0])
            for sign in (-1, 1)
        ) / 2
        maximally_entangled_information = relative_entropy_to_uniform(choi)
        chi_lower = dimension * t**2 / (2 * (1 + alpha))
        chi_upper = dimension * t**2 / (2 * (1 - alpha))
        assert chi_lower <= pair_information <= chi_upper
        assert count * chi_lower <= maximally_entangled_information <= count * chi_upper
        assert (
            maximally_entangled_information / chi_upper
            >= count * (1 - alpha) / (1 + alpha)
        )
        check_schmidt_inputs(generators, basis, t, alpha)

    output_kind = "commuting" if commuting else "full"
    print(
        f"PASS: {output_kind} output, b={dimension}, a={input_dimension}, "
        f"{count} directions, maximally-entangled/pair ratio "
        f"{maximally_entangled_information / pair_information:.8f}"
    )


if __name__ == "__main__":
    check_example(2, commuting=False)
    check_example(3, commuting=False)
    check_example(3, commuting=True)
