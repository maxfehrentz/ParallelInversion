#!/usr/bin/env python3

# Copyright (c) 2020-2023, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

import os

from common import *

def nerf_synthetic(name, frameidx):
	return {
		"data_dir"      : os.path.join(NERF_DATA_FOLDER, f"nerf_synthetic/{name}"),
		"dataset_train" : "transforms_train.json",
		"dataset_test"  : "transforms_test.json",
		"dataset"       : "",
		"frameidx"      : frameidx
	}

# Copy from llff paper
def nerf_llff(name, frameidx):
	return {
		"data_dir"      : os.path.join(NERF_DATA_FOLDER, f"nerf_llff_data/{name}"),
		"dataset_train" : "transforms_train.json",
		"dataset_test"  : "transforms_test.json",
		"dataset"       : "",
		"frameidx"      : frameidx
	}

def MICCAI_hypernet(name, frameidx):
	return {
		"data_dir"      : f"/home/maximilian_fehrentz/Documents/MICCAI/{name}/data/ngp",
		"dataset_train" : "transforms.json",
		"dataset_test"  : "transforms.json",
		"dataset"       : "",
		"frameidx"      : frameidx
	}

def MICCAI_mri(name, frameidx):
	return {
		"data_dir"      : f"/home/maximilian_fehrentz/Documents/MICCAI/{name}/data/ngp_mri",
		"dataset_train" : "transforms.json",
		"dataset_test"  : "transforms.json",
		"dataset"       : "",
		"frameidx"      : frameidx
	}

# Some official dataset
scenes_nerf = {
	# nerf synthetic
	"lego"      : nerf_synthetic("lego", frameidx=52),
	"drums"     : nerf_synthetic("drums", frameidx=52),
	"ship"      : nerf_synthetic("ship", frameidx=52),
	"mic"       : nerf_synthetic("mic", frameidx=52),
	"ficus"     : nerf_synthetic("ficus", frameidx=52),
	"chair"     : nerf_synthetic("chair", frameidx=52),
	"hotdog"    : nerf_synthetic("hotdog", frameidx=52),
	"materials" : nerf_synthetic("materials", frameidx=52),

	# llff
	"fern" : nerf_llff("fern", frameidx=0),
	"flower" : nerf_llff("flower", frameidx=0),
	"fortress" : nerf_llff("fortress", frameidx=0),
	"horns" : nerf_llff("horns", frameidx=0),
	"leaves" : nerf_llff("leaves", frameidx=0),
	"orchids" : nerf_llff("orchids", frameidx=0),
	"room" : nerf_llff("room", frameidx=0),
	"trex" : nerf_llff("trex", frameidx=0),

	# MICCAI cases
	"case003": MICCAI_hypernet("003", frameidx=0),
	"case003_mri": MICCAI_mri("003", frameidx=0),

	"case065": MICCAI_hypernet("065", frameidx=0),
	"case065_mri": MICCAI_mri("065", frameidx=0),

	"case089": MICCAI_hypernet("089", frameidx=0),
	"case089_mri": MICCAI_mri("089", frameidx=0),

	"case207": MICCAI_hypernet("207", frameidx=0),
	"case207_mri": MICCAI_mri("207", frameidx=0),

	"case209": MICCAI_hypernet("209", frameidx=0),
	"case209_mri": MICCAI_mri("209", frameidx=0),
}

