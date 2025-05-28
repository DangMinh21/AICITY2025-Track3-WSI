# You can also use `huggingface-cli download`
# git clone https://huggingface.co/datasets/nvidia/PhysicalAI-Spatial-Intelligence-Warehouse
cd data/PhysicalAI-Spatial-Intelligence-Warehouse

# we need to untar images for train/test subsets
for dir in train test; do
    for subdir in images depths; do
        if [ -d "$dir/$subdir" ]; then
            echo "Processing $dir/$subdir"
            cd "$dir/$subdir"
            tar -xzf chunk_*.tar.gz
            # rm chunk_*.tar.gz
            cd ../..
        fi
    done
done
