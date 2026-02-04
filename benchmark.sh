#!/bin/bash
set -euo pipefail

SETUP_FILES=500

setup_data() {
  mkdir -p bench_data
  cd bench_data
  rm -f *
  for i in $(seq 1 $SETUP_FILES); do
    touch "image_$i.webp"
    touch "image_$i.png"
  done
  cd ..
}

remove_originals() {
  local basename=$1
  rm -f "$basename".{png,jpg,jpeg,gif}
}

echo "Setting up $SETUP_FILES files..."
setup_data

echo "Running baseline..."
start_time=$(date +%s%3N)
count=0
cd bench_data
while IFS= read -r -d '' webp_file; do
  remove_originals "${webp_file%.webp}"
  ((count++)) || true
done < <(find . -name "*.webp" -type f -print0)
cd ..
end_time=$(date +%s%3N)
duration=$((end_time - start_time))
echo "Baseline: $duration ms (processed $count items)"

echo "Setting up files again..."
setup_data

echo "Running optimized..."
start_time=$(date +%s%3N)
count_opt=0
cd bench_data

# Optimization Implementation
# Using mapfile to read all files and process in batches
mapfile -d '' -t webp_files < <(find . -name "*.webp" -type f -print0)
total_files=${#webp_files[@]}
chunk_size=100

for ((i=0; i<total_files; i+=chunk_size)); do
  # Get slice of array
  batch=("${webp_files[@]:i:chunk_size}")
  files_to_delete=()
  for f in "${batch[@]}"; do
    base="${f%.webp}"
    files_to_delete+=("$base.png" "$base.jpg" "$base.jpeg" "$base.gif")
    ((count_opt++)) || true
  done
  # Only run rm if we have files to delete
  if [[ ${#files_to_delete[@]} -gt 0 ]]; then
    rm -f "${files_to_delete[@]}"
  fi
done

cd ..
end_time=$(date +%s%3N)
duration_opt=$((end_time - start_time))
echo "Optimized: $duration_opt ms (processed $count_opt items)"

echo "Speedup: $((duration / duration_opt))x"
