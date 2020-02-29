import math

# Global Parameters
scale_factor = 10
trial_count = 5
sample_count = 10

# Given Base Cases
magnitude_a1 = 2
magnitude_a2 = 3
a1_dot_a2 = 5

# Sampling & Summations
samples = {}
results = {}


# (a . b) = |a||b|cos(theta)
# Therefore,
# theta = cos^-1([a . b] / [|a|*|b|])
def func_theta(a_dot_b, magnitude_a, magnitude_b):
    return math.degrees(math.acos(a_dot_b / (magnitude_a * magnitude_b)))


# (a . b) = |a||b|cos(theta)
# Therefore,
# ([a . b] / |a|) = |b| * cos(theta)
# Vector Projection B Onto A:
# ([a . b] / |a|) * (a / |a|)
# Magnitude Unit Vector A:
# |(a / |a|)| = sqrt(x^2 + y^2 + z^2) = 1
# Therefore,
# |([a . b] / |a|) * (a / |a|)| = |([a . b] / |a|)| * 1
# Scalar Projection B Onto A:
# ([a . b] / |a|) = |([a . b] / |a|)| * 1
# Therefore,
# Magnitude Vector Projection B Onto A:
# |([a . b] / |a|) * (a / |a|)| = |b| * cos(theta)
def func_magnitude_vector_projection(magnitude_b, theta):
    return magnitude_b * math.cos(math.radians(theta))


# Sum From N=1 To Infinity
# Magnitude Vector Projection An-1 Onto An-2:
# |([An-2 . An-1] / |An-2|) * (An-2 / |An-2|)|
# Generalization:
# For N = 1, |An| = 2
# For N = 2, |An| = 3
# For N > 2, |An| = |An-1| * cos(theta)
# For N > 2, |An| = |An=2| * cos^n-2(theta)
# Where theta = cos^-1([An=1 . An=2] / [|An=1| * |An=2|])
# Therefore,
# For N > 1, |An| = |An=2| * ([An=1 . An=2] / [|An=1| * |An=2|])^(n-2)
# P + Q(M / PQ)^(N - 2) ....
def proc_estimate_infinite_summation(begin, end, theta, trial_id):
    samples[trial_id] = []
    sample_modulus = math.ceil(end / sample_count)

    n_minus_one = 0
    summation = 0

    for n in range(begin, end + 1):
        if n is 1:
            n_minus_one = magnitude_a1
        elif n is 2:
            n_minus_one = magnitude_a2
        else:
            n_minus_one = func_magnitude_vector_projection(magnitude_b=n_minus_one,
                                                           theta=theta)
        summation += n_minus_one

        if n % sample_modulus is 0:
            samples[trial_id].append({n_minus_one: summation})

    results[trial_id] = summation


if __name__ == '__main__':

    a_theta_b = func_theta(a1_dot_a2, magnitude_a1, magnitude_a2)

    for ID in range(1, trial_count + 1):
        proc_estimate_infinite_summation(begin=1,
                                         end=int(math.pow(scale_factor, ID)),
                                         theta=a_theta_b,
                                         trial_id=ID)

    print('{Trial Id: Sum ->> [{Nth Term Magnitude: Nth Partial Sum]}')
    for trial in results:
        print('{0}: {1:0.8F} {2:>3} {3}'.format(trial,
                                                results[trial],
                                                '->>',
                                                samples[trial]))
