"""Finite checks for the joint input/output dimension and weak-signal laws."""

from itertools import product

import numpy as np

from check_sharp_output import clifford_generators, entropy, tensor_product, traceless_basis


def bkm_weights(spectrum):
    left = spectrum[:, None]
    right = spectrum[None, :]
    difference = left - right
    separated = np.abs(difference) > 1e-8 * np.maximum(left, right)
    return np.divide(
        np.log(left) - np.log(right), difference, out=2 / (left + right), where=separated
    )


def perturbations(weights, observables, directions):
    root_weights = np.sqrt(weights)
    joint = sum(
        np.kron(root_weights[:, None] * observable.T * root_weights, direction)
        for observable, direction in zip(observables, directions)
    )
    marginal = sum(
        np.dot(weights, observable.diagonal()) * direction
        for observable, direction in zip(observables, directions)
    )
    return joint, marginal


def check_exact_input_coefficient():
    rng = np.random.default_rng(20261124)
    for input_dimension, output_dimension in [(2, 2), (3, 4)]:
        observables = traceless_basis(input_dimension, commuting=False)
        count = len(observables)
        directions = traceless_basis(output_dimension, commuting=False)[:count]
        radius_squared = 1 - 1 / input_dimension
        for rank in range(1, input_dimension + 1):
            weights = np.geomspace(0.01, 1, rank)
            weights /= weights.sum()
            vectors = rng.normal(size=(input_dimension, rank)) + 1j * rng.normal(
                size=(input_dimension, rank)
            )
            vectors, _ = np.linalg.qr(vectors)
            compressed = np.array([vectors.conj().T @ matrix @ vectors for matrix in observables])
            joint, marginal = perturbations(weights, compressed, directions)
            centered = joint - np.kron(np.diag(weights), marginal)
            product_spectrum = np.repeat(weights / output_dimension, output_dimension)
            joint_coefficient = np.sum(bkm_weights(product_spectrum) * np.abs(centered)**2)
            coordinate_coefficient = np.sum(
                bkm_weights(weights) * np.outer(weights, weights) * np.abs(compressed)**2
            ) - np.sum(np.abs(marginal)**2)
            np.testing.assert_allclose(joint_coefficient, output_dimension * coordinate_coefficient,
                                       rtol=1e-10, atol=1e-11)
            assert 0 <= joint_coefficient <= output_dimension * min(count, rank + 1) * radius_squared
            if rank == 1:
                np.testing.assert_allclose(joint_coefficient, 0, atol=1e-25)

        uniform = np.full(input_dimension, 1 / input_dimension)
        joint, marginal = perturbations(uniform, observables, directions)
        np.testing.assert_allclose(marginal, 0, atol=1e-12)
        ratio = input_dimension * np.sum(np.abs(joint)**2) / radius_squared
        np.testing.assert_allclose(ratio, input_dimension + 1, atol=1e-12)
        print(f"PASS: exact uniform-base coefficient {ratio:.0f} at a={input_dimension}, b={output_dimension}")


def symmetric_square_radius_upper(observables):
    dimension = observables[0].shape[0]
    vectors = []
    for row in range(dimension):
        for column in range(row, dimension):
            vector = np.zeros((dimension, dimension))
            vector[row, column] = vector[column, row] = 1
            vectors.append(vector.ravel() / np.linalg.norm(vector))
    basis = np.array(vectors).T
    quadratic = sum(np.kron(matrix, matrix) for matrix in observables)
    return np.linalg.eigvalsh(basis.T @ quadratic @ basis)[-1]


def check_gaussian_witness():
    input_dimension = 9
    output_dimension = 3
    count = output_dimension**2 - 1
    rng = np.random.default_rng(20261125)
    coordinates = rng.normal(size=(count, input_dimension**2 - 1)) / np.sqrt(input_dimension)
    observables = np.einsum('ij,jkl->ikl', coordinates, traceless_basis(input_dimension, False))
    radius_upper = symmetric_square_radius_upper(observables)
    coefficient = np.sum(np.abs(observables)**2) / input_dimension
    assert radius_upper < 12**2 and coefficient >= 3 * count / 8

    output_spectrum = np.array([0.13, 0.34, 0.53])
    base_output = np.diag(output_spectrum)
    basis = traceless_basis(output_dimension, commuting=False)
    output_metric = bkm_weights(output_spectrum)
    gram = np.einsum('jxy,xy,kxy->jk', np.conjugate(basis), output_metric, basis).real
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    directions = np.einsum('ij,jxy->ixy', (eigenvectors / np.sqrt(eigenvalues)) @ eigenvectors.T, basis)
    np.testing.assert_allclose(
        np.einsum('jxy,xy,kxy->jk', directions.conj(), output_metric, directions),
        np.eye(count), atol=1e-12,
    )

    for rank in (2, 4, input_dimension):
        weights = np.geomspace(0.001, 1, rank)
        weights /= weights.sum()
        compressed = observables[:, :rank, :rank]
        joint, _ = perturbations(weights, compressed, directions)
        product_spectrum = np.outer(weights, output_spectrum).ravel()
        joint_coefficient = np.sum(bkm_weights(product_spectrum) * np.abs(joint)**2)
        assert joint_coefficient <= min(2 * count, 4 * rank - 3) * radius_upper

    uniform = np.full(input_dimension, 1 / input_dimension)
    joint, marginal = perturbations(uniform, observables, directions)
    np.testing.assert_allclose(marginal, 0, atol=1e-12)
    product_spectrum = np.outer(uniform, output_spectrum).ravel()
    np.testing.assert_allclose(np.sum(bkm_weights(product_spectrum) * np.abs(joint)**2),
                               coefficient, atol=1e-12)

    scale = np.max(np.abs(np.linalg.eigvalsh(observables)))
    root_inverse = np.diag(1 / np.sqrt(output_spectrum))
    relative_size = np.max(np.abs(np.linalg.eigvalsh(root_inverse @ directions @ root_inverse)))
    alpha = 0.1
    signal = alpha / (count * scale * relative_size)
    identity = np.eye(input_dimension)
    effects = [(identity + sign * matrix / scale) / (2 * count)
               for matrix in observables for sign in (-1, 1)]
    preparations = [base_output + sign * signal * count * scale * direction
                    for direction in directions for sign in (-1, 1)]
    np.testing.assert_allclose(sum(effects), identity, atol=1e-12)
    np.testing.assert_allclose([np.trace(state) for state in preparations], 1, atol=1e-12)
    assert np.min(np.linalg.eigvalsh(effects)) >= -1e-12
    assert np.min(np.linalg.eigvalsh(preparations)) > 0
    choi = np.diag(product_spectrum) + signal * joint
    np.testing.assert_allclose(
        choi, sum(np.kron(effect.T, state) for effect, state in zip(effects, preparations)) / input_dimension,
        atol=1e-12,
    )

    information = np.log(input_dimension) + entropy(base_output) - entropy(choi)
    lead = signal**2 * coefficient / 2
    assert lead / (1 + alpha) <= information <= lead / (1 - alpha)
    ordinary_upper = signal**2 * radius_upper / (2 * (1 - alpha))
    lower_ratio = information / ordinary_upper
    assert lower_ratio > 1
    print(f"PASS: finite Gaussian witness at a=9, b=3, ratio lower certificate {lower_ratio:.3f}")

    weights = np.array([0.001, 0.299, 0.7])
    reference = np.diag(weights)
    joint, marginal = perturbations(weights, observables[:, :3, :3], directions)
    centered = joint - np.kron(reference, marginal)
    product_spectrum = np.outer(weights, output_spectrum).ravel()
    centered_coefficient = np.sum(bkm_weights(product_spectrum) * np.abs(centered)**2)
    joint_state = np.diag(product_spectrum) + signal * joint
    output_state = base_output + signal * marginal
    information = entropy(reference) + entropy(output_state) - entropy(joint_state)
    lead = signal**2 * centered_coefficient / 2
    assert lead / (1 + alpha) <= information <= lead / (1 - alpha)
    print("PASS: finite Hessian bounds at an uneven rank-three Schmidt input")


def check_minimal_clifford_dimensions():
    for count in range(2, 8):
        pairs = count // 2
        observables = clifford_generators(2 * pairs)
        if count % 2:
            observables.append(tensor_product([np.diag([1, -1])] * pairs))
        identity = np.eye(2**pairs)
        for row, column in product(range(count), repeat=2):
            first, second = observables[row], observables[column]
            np.testing.assert_allclose(first @ second + second @ first, 2 * (row == column) * identity)
        involutions = [1j * observables[2 * pair] @ observables[2 * pair + 1]
                       for pair in range(pairs)]
        for signs in product((-1, 1), repeat=pairs):
            projector = identity
            for sign, involution in zip(signs, involutions):
                projector = projector @ ((identity + sign * involution) / 2)
            np.testing.assert_allclose(np.trace(projector), 1)
        np.testing.assert_allclose(sum(np.trace(matrix @ matrix).real for matrix in observables) /
                                   len(identity), count)
    print("PASS: minimal Clifford witnesses and sign sectors for 2 through 7 directions")


if __name__ == '__main__':
    check_exact_input_coefficient()
    check_gaussian_witness()
    check_minimal_clifford_dimensions()
