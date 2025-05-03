import uuid, argparse, os
#import uuid, argparse, os, shutil

class NULL_NAMESPACE:
    """This garbage is needed to replicate the behavior of the UUID.nameUUIDfromBytes function present in Java."""
    bytes = b''
def get_offline_uuid(player: str):
    """Return the *offline* UUID of a player name"""
    return uuid.uuid3(NULL_NAMESPACE, f'OfflinePlayer:{player}')



def replace_uuid(old_uuid: str, new_uuid: str, path):
    
    if not (os.path.exists(path)):
        print (f"World path not exist: {path}")
        exit(1)

    folders = ["advancements", "playerdata", "stats"]
    for folder in folders:
        if not (os.path.exists(f"{path}/{folder}")):
            print (f"folder '{folder}' not found")
            exit(1)

        extensions = [".dat", ".dat_old", ".json"]
        for extension in extensions:
            if (os.path.exists(f"{path}/{folder}/{old_uuid}{extension}")):
                #shutil.copyfile(f"{path}/{folder}/{old_uuid}{extension}", f"{path}/{folder}/{old_uuid}{extension}-backup")
                os.rename(f"{path}/{folder}/{old_uuid}{extension}", f"{path}/{folder}/{new_uuid}{extension}")
            



if __name__ == '__main__':

    parser=argparse.ArgumentParser()
    parser.add_argument("--old", help="Old nickname")
    parser.add_argument("--new", help="New nickname")
    parser.add_argument("--worldpath", help="World Path")
    args=parser.parse_args()
    
    old_uuid = get_offline_uuid(args.old)
    new_uuid = get_offline_uuid(args.new)
    world_path = args.worldpath

    replace_uuid(old_uuid, new_uuid, world_path)






    #print(f"--old: {args.old}")
    #print(f"--new: {args.new}")
    #print(f"--serverpath: {args.serverpath}")
    #print(f"Dict format: {vars(args)}")