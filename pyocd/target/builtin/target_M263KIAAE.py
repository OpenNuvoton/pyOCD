# pyOCD debugger
# Copyright (c) 2019 Arm Limited
# SPDX-License-Identifier: Apache-2.0
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

from ...flash.flash import Flash
from ...core.coresight_target import CoreSightTarget
from ...core.memory_map import (FlashRegion, RamRegion, MemoryMap)
from ...debug.svd.loader import SVDFile

FLASH_ALGO_AP_512 = {
    'load_address' : 0x20000000,
    'instructions': [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0xb087b5b0, 0x460c4613, 0x90054605, 0x92039104, 0x94019302, 0xe7ff9500, 0x6800481f, 0x42082101,
    0xe7ffd001, 0x481de7f8, 0x22406801, 0x60014311, 0x491b9805, 0x98046008, 0x6008491a, 0x28009803,
    0xe7ffd105, 0x43c02000, 0x60084917, 0x4816e003, 0x60014916, 0x4816e7ff, 0x60012101, 0x8f6ff3bf,
    0x480de7ff, 0x21016800, 0xd0014208, 0xe7f8e7ff, 0x6800480a, 0x42082140, 0xe7ffd008, 0x68014807,
    0x43112240, 0x20016001, 0xe0029006, 0x90062000, 0x9806e7ff, 0xbdb0b007, 0x4000c0c0, 0x4000c000,
    0x4000c00c, 0x4000c004, 0x4000c008, 0x0055aa03, 0x4000c010, 0xb087b5b0, 0x460c4613, 0x90054605,
    0x92039104, 0x2159481d, 0x21166001, 0x21886001, 0x68006001, 0x42082101, 0x94019302, 0xd1039500,
    0x2001e7ff, 0xe0269006, 0x68014815, 0x43112204, 0x48146001, 0x43116801, 0xe7ff6001, 0x68004812,
    0x42082110, 0xe7ffd101, 0x4810e7f8, 0x22016801, 0x60014311, 0x600a490e, 0x42106800, 0xe7ffd103,
    0x90062001, 0x4809e007, 0x22406801, 0x60014311, 0x90062000, 0x9806e7ff, 0xbdb0b007, 0x40000100,
    0x40000200, 0x40000204, 0x40000250, 0x4000c000, 0x4000c01c, 0x4601b082, 0x91009001, 0x4809e7ff,
    0x21016800, 0xd0014208, 0xe7f8e7ff, 0x68014806, 0x43912201, 0x48056001, 0x60012100, 0xb0024608,
    0x46c04770, 0x4000c0c0, 0x4000c000, 0x4000c01c, 0xb084b580, 0x90034601, 0x22019803, 0x43980713,
    0x98039003, 0x40184b0e, 0x98039003, 0x051b230f, 0x05524018, 0x91014290, 0xe7ffd107, 0x49099803,
    0x90031840, 0x90022001, 0x2000e002, 0xe7ff9002, 0x9a029903, 0xf7ff2022, 0xb004ff13, 0x46c0bd80,
    0xfffff800, 0xffe00000, 0xb086b580, 0x4603460a, 0x91039004, 0x90022000, 0x93009201, 0x9802e7ff,
    0x42889903, 0xe7ffd20f, 0x99029804, 0x92021c4a, 0x58400089, 0xffbcf7ff, 0xd0032800, 0x2001e7ff,
    0xe0039005, 0x2000e7eb, 0xe7ff9005, 0xb0069805, 0x46c0bd80, 0xb087b5b0, 0x460c4613, 0x90054605,
    0x92039104, 0x1cc09804, 0x43882103, 0x98059004, 0x07092101, 0x90054388, 0x94019302, 0xe7ff9500,
    0x68004822, 0x42082101, 0xe7ffd001, 0x4820e7f8, 0x22406801, 0x60014311, 0x2121481e, 0xe7ff6001,
    0x28009804, 0xe7ffd02c, 0x491b9805, 0x98036008, 0x491a6800, 0x481a6008, 0x60012101, 0x8f6ff3bf,
    0x4812e7ff, 0x21016800, 0xd0014208, 0xe7f8e7ff, 0x6800480f, 0x42082140, 0xe7ffd008, 0x6801480c,
    0x43112240, 0x20016001, 0xe00c9006, 0x1d009805, 0x98039005, 0x90031d00, 0x1f009804, 0xe7cf9004,
    0x90062000, 0x9806e7ff, 0xbdb0b007, 0x4000c0c0, 0x4000c000, 0x4000c00c, 0x4000c004, 0x4000c008,
    0x4000c010, 0xb088b5b0, 0x460c4613, 0x90064605, 0x92049105, 0x1cc09805, 0x43882103, 0x98069005,
    0x07092101, 0x90034008, 0x43889806, 0x93029006, 0x95009401, 0x4826e7ff, 0x21016800, 0xd0014208,
    0xe7f8e7ff, 0x68014823, 0x43112240, 0x48226001, 0x60012100, 0x9805e7ff, 0xd0322800, 0x9806e7ff,
    0x6008491e, 0x2101481e, 0xf3bf6001, 0xe7ff8f6f, 0x68004817, 0x42082101, 0xe7ffd001, 0x4815e7f8,
    0x21406800, 0xd0084208, 0x4812e7ff, 0x22406801, 0x60014311, 0x90072001, 0x4812e016, 0x99046800,
    0x42886809, 0xe7ffd003, 0x90072001, 0x9806e00c, 0x90061d00, 0x1d009804, 0x98059004, 0x90051f00,
    0x2000e7c9, 0xe7ff9007, 0xb0089807, 0x46c0bdb0, 0x4000c0c0, 0x4000c000, 0x4000c00c, 0x4000c004,
    0x4000c010, 0x4000c008, 0x00000000
    ],

    # Relative function addresses
    'pc_init': 0x200000d5,
    'pc_unInit': 0x20000175,
    'pc_program_page': 0x20000255,
    'pc_erase_sector': 0x200001b1,
    'pc_eraseAll': 0x0,

    'static_base' : 0x20000000 + 0x00000020 + 0x000003e8,
    'begin_stack' : 0x20000700,
    'begin_data' : 0x20000000 + 0x1000,
    'page_size' : 0x800,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000,
    'page_buffers' : [0x20001000, 0x20001800],   # Enable double buffering
    'min_program_length' : 0x800,

    # Flash information
    'flash_start': 0x0,
    'flash_size': 0x80000,
    'sector_sizes': (
        (0x0, 0x800),
    )
}

FLASH_ALGO_LD_4 = {
    'load_address' : 0x20000000,
    'instructions': [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0xb087b5b0, 0x460c4613, 0x90054605, 0x92039104, 0x94019302, 0xe7ff9500, 0x6800481f, 0x42082101,
    0xe7ffd001, 0x481de7f8, 0x22406801, 0x60014311, 0x491b9805, 0x98046008, 0x6008491a, 0x28009803,
    0xe7ffd105, 0x43c02000, 0x60084917, 0x4816e003, 0x60014916, 0x4816e7ff, 0x60012101, 0x8f6ff3bf,
    0x480de7ff, 0x21016800, 0xd0014208, 0xe7f8e7ff, 0x6800480a, 0x42082140, 0xe7ffd008, 0x68014807,
    0x43112240, 0x20016001, 0xe0029006, 0x90062000, 0x9806e7ff, 0xbdb0b007, 0x4000c0c0, 0x4000c000,
    0x4000c00c, 0x4000c004, 0x4000c008, 0x0055aa03, 0x4000c010, 0xb087b5b0, 0x460c4613, 0x90054605,
    0x92039104, 0x2159481d, 0x21166001, 0x21886001, 0x68006001, 0x42082101, 0x94019302, 0xd1039500,
    0x2001e7ff, 0xe0269006, 0x68014815, 0x43112204, 0x48146001, 0x43116801, 0xe7ff6001, 0x68004812,
    0x42082110, 0xe7ffd101, 0x4810e7f8, 0x22016801, 0x60014311, 0x600a490e, 0x42106800, 0xe7ffd103,
    0x90062001, 0x4809e007, 0x22406801, 0x60014311, 0x90062000, 0x9806e7ff, 0xbdb0b007, 0x40000100,
    0x40000200, 0x40000204, 0x40000250, 0x4000c000, 0x4000c01c, 0x4601b082, 0x91009001, 0x4809e7ff,
    0x21016800, 0xd0014208, 0xe7f8e7ff, 0x68014806, 0x43912201, 0x48056001, 0x60012100, 0xb0024608,
    0x46c04770, 0x4000c0c0, 0x4000c000, 0x4000c01c, 0xb084b580, 0x90034601, 0x22019803, 0x43980713,
    0x98039003, 0x40184b0e, 0x98039003, 0x051b230f, 0x05524018, 0x91014290, 0xe7ffd107, 0x49099803,
    0x90031840, 0x90022001, 0x2000e002, 0xe7ff9002, 0x9a029903, 0xf7ff2022, 0xb004ff13, 0x46c0bd80,
    0xfffff800, 0xffe00000, 0xb086b580, 0x4603460a, 0x91039004, 0x90022000, 0x93009201, 0x9802e7ff,
    0x42889903, 0xe7ffd20f, 0x99029804, 0x92021c4a, 0x58400089, 0xffbcf7ff, 0xd0032800, 0x2001e7ff,
    0xe0039005, 0x2000e7eb, 0xe7ff9005, 0xb0069805, 0x46c0bd80, 0xb087b5b0, 0x460c4613, 0x90054605,
    0x92039104, 0x1cc09804, 0x43882103, 0x98059004, 0x07092101, 0x90054388, 0x94019302, 0xe7ff9500,
    0x68004822, 0x42082101, 0xe7ffd001, 0x4820e7f8, 0x22406801, 0x60014311, 0x2121481e, 0xe7ff6001,
    0x28009804, 0xe7ffd02c, 0x491b9805, 0x98036008, 0x491a6800, 0x481a6008, 0x60012101, 0x8f6ff3bf,
    0x4812e7ff, 0x21016800, 0xd0014208, 0xe7f8e7ff, 0x6800480f, 0x42082140, 0xe7ffd008, 0x6801480c,
    0x43112240, 0x20016001, 0xe00c9006, 0x1d009805, 0x98039005, 0x90031d00, 0x1f009804, 0xe7cf9004,
    0x90062000, 0x9806e7ff, 0xbdb0b007, 0x4000c0c0, 0x4000c000, 0x4000c00c, 0x4000c004, 0x4000c008,
    0x4000c010, 0xb088b5b0, 0x460c4613, 0x90064605, 0x92049105, 0x1cc09805, 0x43882103, 0x98069005,
    0x07092101, 0x90034008, 0x43889806, 0x93029006, 0x95009401, 0x4826e7ff, 0x21016800, 0xd0014208,
    0xe7f8e7ff, 0x68014823, 0x43112240, 0x48226001, 0x60012100, 0x9805e7ff, 0xd0322800, 0x9806e7ff,
    0x6008491e, 0x2101481e, 0xf3bf6001, 0xe7ff8f6f, 0x68004817, 0x42082101, 0xe7ffd001, 0x4815e7f8,
    0x21406800, 0xd0084208, 0x4812e7ff, 0x22406801, 0x60014311, 0x90072001, 0x4812e016, 0x99046800,
    0x42886809, 0xe7ffd003, 0x90072001, 0x9806e00c, 0x90061d00, 0x1d009804, 0x98059004, 0x90051f00,
    0x2000e7c9, 0xe7ff9007, 0xb0089807, 0x46c0bdb0, 0x4000c0c0, 0x4000c000, 0x4000c00c, 0x4000c004,
    0x4000c010, 0x4000c008, 0x00000000
    ],

    # Relative function addresses
    'pc_init': 0x200000d5,
    'pc_unInit': 0x20000175,
    'pc_program_page': 0x20000255,
    'pc_erase_sector': 0x200001b1,
    'pc_eraseAll': 0x0,

    'static_base' : 0x20000000 + 0x00000020 + 0x000003e8,
    'begin_stack' : 0x20000700,
    'begin_data' : 0x20000000 + 0x1000,
    'page_size' : 0x800,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000,
    'page_buffers' : [0x20001000, 0x20001800],   # Enable double buffering
    'min_program_length' : 0x800,

    # Flash information
    'flash_start': 0x100000,
    'flash_size': 0x1000,
    'sector_sizes': (
        (0x0, 0x800),
    )
}

class M263KIAAE(CoreSightTarget):
    VENDOR = "Nuvoton"

    memoryMap = MemoryMap(
        FlashRegion( start=0x00000000, length=0x80000,  sector_size=0x0800,
                                                        page_size=0x0800,
                                                        is_boot_memory=True,
                                                        algo=FLASH_ALGO_AP_512),
        FlashRegion( start=0x00100000, length=0x1000,   sector_size=0x0800,
                                                        page_size=0x0800,
                                                        algo=FLASH_ALGO_LD_4),
        RamRegion(   start=0x20000000, length=0x18000)
        )

    def __init__(self, link):
        super(M263KIAAE, self).__init__(link, self.memoryMap)
        self._svd_location = SVDFile.from_builtin("M261_v1.svd")
