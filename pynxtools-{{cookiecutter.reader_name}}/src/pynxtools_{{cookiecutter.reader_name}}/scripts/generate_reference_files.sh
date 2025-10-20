#!/bin/bash
READER={{cookiecutter.reader_name}}
NXDL={{cookiecutter.supported_nxdls}}

project_dir=$(dirname $(dirname $(realpath $0)))
cd $project_dir/tests/data

function update_ref_file {
  local FOLDER=$1
  local NXDL=$2
  echo "Update $FOLDER reference file for $NXDL"
  files=$(find . -type f \( ! -name "*.log" -a ! -name "*.nxs" \))
  dataconverter ${files[@]} --reader $READER --nxdl $NXDL --ignore-undocumented --output "$FOLDER_ $NXDL_ref.nxs" &> ref_output.txt
  cd ..
}

project_dir=$(dirname $(dirname $(realpath $0)))

folders=(
  ""
)

nxdls={{cookiecutter.supported_nxdls}}

for folder in "${folders[@]}"; do
  for nxdl in "${nxdls[@]}"; do
    cd $project_dir/tests/data
    update_ref_file "$folder" "$nxdl"
  done
done