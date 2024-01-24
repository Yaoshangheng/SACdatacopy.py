#!/bin/bash

# 源数据文件夹路径
source_folder="/run/media/yaoyuan/data5/2018_new"

# 目标数据文件夹路径
destination_folder="/path/to/destination/folder"

# 遍历所有台站目录
for station_path in "$source_folder"/*; do
    # 检查是否是目录
    if [ -d "$station_path" ]; then
        # 遍历年份目录
        for year_path in "$station_path"/*; do
            # 检查是否是目录
            if [ -d "$year_path" ]; then
                # 遍历日期文件夹
                for date_path in "$year_path"/*; do
                    # 检查是否是目录
                    if [ -d "$date_path" ]; then
                        # 获取日期文件夹中的文件列表
                        files_to_copy=("$date_path"/*)

                        # 构建目标日期文件夹的路径
                        destination_date_path="$destination_folder/$(basename "$date_path")"

                        # 如果目标日期文件夹不存在，则创建
                        [ -d "$destination_date_path" ] || mkdir -p "$destination_date_path"

                        # 拷贝文件
                        echo "Copying files for $(basename "$date_path")"
                        cp -r "${files_to_copy[@]}" "$destination_date_path"
                    fi
                done
            fi
        done
    fi
done
