import uuid, argparse, os

class NULL_NAMESPACE:
    """This garbage is needed to replicate the behavior of the UUID.nameUUIDfromBytes function present in Java."""
    bytes = b''
def get_offline_uuid(player: str):
    """Return the *offline* UUID of a player name"""
    return uuid.uuid3(NULL_NAMESPACE, f'OfflinePlayer:{player}')



def replace_uuid(old_uuid: str, new_uuid: str, path):

    folders = ["advancements", "playerdata", "stats"]
    extensions = [".dat", ".dat_old", ".json"]

    for folder in folders:
        if not (os.path.exists(f"{path}/{folder}")):
            print (f"folder '{folder}' not found")
            exit(1)

        for extension in extensions:  
                
            old_file_path = f"{path}/{folder}/{old_uuid}{extension}".replace('//', '/')
            new_file_path = f"{path}/{folder}/{new_uuid}{extension}".replace('//', '/')      
            
            if (os.path.exists(old_file_path)):
                print(f"file renamed: {new_file_path}")
                os.rename(old_file_path, new_file_path)
            #else:
            #    print(f"file not found: {old_file_path}")



if __name__ == '__main__':

    parser=argparse.ArgumentParser()
    parser.add_argument("--old", help="Old nickname")
    parser.add_argument("--new", help="New nickname")
    parser.add_argument("--worldpath", help="World Path")
    args=parser.parse_args()
    
    old_uuid = get_offline_uuid(args.old)
    new_uuid = get_offline_uuid(args.new)
    world_path = args.worldpath
    print(f'old name {args.old} - {old_uuid}')
    print(f'new name {args.new} - {new_uuid}')
    replace_uuid(old_uuid, new_uuid, world_path)
