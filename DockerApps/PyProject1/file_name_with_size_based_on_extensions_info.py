"""To get the File NAME and SIZE of each File w.r.t their Extensions in a Given Folder

Display the File NAME and SIZE of each FILE w.r.t their EXTENSION 
"""

from collections import defaultdict
import os 
from datetime import datetime

# INPUT_DIR_PATH = r"D:\Sairam\ODWA4_20240114_T82q0z\TERRAFORM"

def get_files_data_based_on_extension(dir_path):
    '''To find the FileNAME and SIZE of each Files w.r.t. their Extensions..'''

    print("You have supplied Folder: ", dir_path)
    filelist = []
    extn_dict = defaultdict(list)
    
    for root_dir, sub_dirs, files in os.walk(dir_path):
        print(f"{root_dir = } has {len(sub_dirs)} Sub-Dir's..")
        for file in files:
            # print(file)
            filename = os.path.join(root_dir, file)
            if os.path.isfile(filename):
                fname, extn = os.path.splitext(filename)
                # if extn not in extn_dict:
                #     extn_dict[extn] = 0
                fsize = os.stat(filename).st_size
                fsize_byt = fsize
                fsize_kbs = fsize / 1024
                fsize_mbs = fsize / (1024 * 1024)
                fsize_gbs = fsize / (1024 * 1024 * 1024)
                
                file_tuple = (filename, fsize_byt, fsize_kbs, fsize_mbs, fsize_gbs)
                extn_dict[extn].append(file_tuple) 

    # print("The Memory SIZE of Files w.r.t their File Extension are as below:")
    # print(extn_dict)
    return extn_dict


def write_data_into_file(extn_dict):
    '''To write the Data into the File'''
    # The following are the File Info for the Extension: ".txt"
    #File Headers: FileName, Size in GB, Size in MB, Size in KB, Size in Bytes
    fname = f"details_of_all_extension_files.log"

    with open(fname, "w") as fw:
        for k_extn, v_data in extn_dict.items():
            fw.write(f"The following are the File Info for the Extension: {k_extn} \n")
            fw.write(f"FileName \t Size in GB \t Size in MB \t Size in KB \t Size in Bytes \n")
            for data in v_data:
                fname, fsize_bytes, fsize_kbs, fsize_mbs, fsize_gbs = data
                fline = f"{fname} \t {fsize_gbs:.3f} GB \t {fsize_mbs:.3f} MB \t {fsize_kbs:.3f} KB \t {fsize_bytes:7d} Bytes\n" 
                fw.write(fline)
            fw.write("\n" + "##" * 25 + "\n")


def write_data_into_separate_extn_file(extn_dict):
    '''To write the Data into the File'''
    # The following are the File Info for the Extension: ".txt"
    #File Headers: FileName, Size in GB, Size in MB, Size in KB, Size in Bytes
    # fname = f"details_of_all_files_with_separate_extns.txt"

    # with open(fname, "w") as fw:
    for k_extn, v_data in extn_dict.items():
        write_info_of_extension_file(k_extn, v_data)


def write_info_of_extension_file(fextn, fdata):
    '''To display and write the info of all extens into a File..'''
    results_folder = "RESULTS"
    if not os.path.isdir(results_folder):
        os.mkdir(results_folder)

    fname = f"{results_folder}\\filenames_sizes_in_DESC_order_with_{fextn[1:]}_extension.log"

    with open(fname, "w") as fwrite:
        fwrite.write(f"The following are the File Info in DESC Order for the Extension: `{fextn}`\n")
        fwrite.write(f"FileName, Size in GB, Size in MB, Size in KB, Size in Bytes \n")
        for data in sorted(fdata, key=lambda x: x[4], reverse= True):
            # Item-0, Item-1,    Item-2,    Item-3,    Item-4   
            fname, fsize_bytes, fsize_kbs, fsize_mbs, fsize_gbs = data
            fline = f"{fname} \t {fsize_gbs:.3f} GB \t {fsize_mbs:.3f} MB \t {fsize_kbs:.3f} KB \t {fsize_bytes:7d} Bytes\n"
            fwrite.write(fline)
        fwrite.write("\n" + "##" * 25 + "\n")


def main():
    reqd_dir_path = input("Enter the existing Valid Folder Full Path: ")
    extns_data = get_files_data_based_on_extension(reqd_dir_path)
    # for fextn, fdata in extns_data.items():
    #     write_info_of_extension_file(fextn, fdata)
    #     print("\n")
    # # write_data_into_file(extns_data)

    write_data_into_separate_extn_file(extns_data)


if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    time_duration = end_time - start_time
    print(f"Time Duration: {time_duration.microseconds}ms -OR- {time_duration.seconds} Seconds")
