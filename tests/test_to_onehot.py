# Copyright 2020 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import numpy as np
import torch
from parameterized import parameterized

from monai.utils.to_onehot import to_onehot

TEST_CASE_1 = [  # single channel 2D, batch 3, shape (2, 1, 2, 2)
    {'data': torch.tensor([[[[0, 1], [1, 2]]], [[[2, 1], [1, 0]]]]), 'num_classes': 3},
    (2, 3, 2, 2),
]

TEST_CASE_2 = [  # single channel 1D, batch 2, shape (2, 1, 4)
    {'data': torch.tensor([[[1, 2, 2, 0]], [[2, 1, 0, 1]]]), 'num_classes': 3},
    (2, 3, 4),
    np.array([[[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0]], [[0, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 0]]]),
]

TEST_CASE_3 = [  # single channel 0D, batch 2, shape (2, 1)
    {'data': torch.tensor([[1.], [2.]]), 'num_classes': 3},
    (2, 3),
    np.array([[0, 1, 0], [0, 0, 1]]),
]


class TestToOneHot(unittest.TestCase):

    @parameterized.expand([TEST_CASE_1, TEST_CASE_2, TEST_CASE_3])
    def test_shape(self, input_data, expected_shape, expected_result=None):
        result = to_onehot(**input_data)
        self.assertEqual(result.shape, expected_shape)
        if expected_result is not None:
            self.assertTrue(np.allclose(expected_result, result.numpy()))


if __name__ == '__main__':
    unittest.main()