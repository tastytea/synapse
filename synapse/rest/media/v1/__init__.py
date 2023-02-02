# Copyright 2014-2016,2023 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PIL.features import check_codec, check_module

# check for JPEG support.
if not check_codec("jpg"):
    raise Exception(
        "FATAL: jpeg codec not supported. Install pillow correctly! "
        " 'sudo apt-get install libjpeg-dev' then 'pip uninstall pillow &&"
        " pip install pillow --user'"
    )


# check for PNG support.
if not check_codec("zlib"):
    raise Exception(
        "FATAL: zip codec not supported. Install pillow correctly! "
        " 'sudo apt-get install zlib1g-dev' then 'pip uninstall pillow &&"
        " pip install pillow --user'"
    )


# check for WebP support.
if not check_module("webp"):
    raise Exception(
        "FATAL: webp module not supported. Install pillow correctly! "
        " 'sudo apt-get install libwebp-dev' then 'pip uninstall pillow &&"
        " pip install pillow --user'"
    )
