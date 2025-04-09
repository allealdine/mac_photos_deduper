from Foundation import NSDate
from Photos import *
import objc
import datetime


def fetch_all_assets():
    options = PHFetchOptions.alloc().init()
    return PHAsset.fetchAssetsWithOptions_(options)


def get_asset_filename(asset):
    resource_class = objc.lookUpClass("PHAssetResource")
    resources = resource_class.assetResourcesForAsset_(asset)
    for res in resources:
        return str(res.originalFilename())  # Some assets may have no name
    return None


def get_asset_creation_date(asset):
    return asset.creationDate()


def delete_assets(assets_to_delete):
    def change_block():
        for asset in assets_to_delete:
            request = PHAssetChangeRequest.deleteAssets_([asset])

    PHPhotoLibrary.sharedPhotoLibrary().performChangesAndWait_error_(change_block, None)


def main():
    all_assets = fetch_all_assets()
    print(f"Total assets: {all_assets.count()}")

    filename_map = {}

    for i in range(all_assets.count()):
        asset = all_assets.objectAtIndex_(i)
        name = get_asset_filename(asset)
        date = get_asset_creation_date(asset)
        if not name or not date:
            continue

        if name not in filename_map:
            filename_map[name] = [asset]
        else:
            filename_map[name].append(asset)

    duplicates_to_delete = []

    for name, assets in filename_map.items():
        if len(assets) > 1:
            # Sort by creation date
            assets_sorted = sorted(
                assets, key=lambda a: a.creationDate().timeIntervalSince1970()
            )
            # Keep oldest, delete the rest
            duplicates_to_delete.extend(assets_sorted[1:])

    print(f"Found {len(duplicates_to_delete)} duplicates to delete.")

    if duplicates_to_delete:
        confirm = input("Are you sure you want to delete them? (yes/no): ")
        if confirm.lower() == "yes":
            delete_assets(duplicates_to_delete)
            print("Duplicates deleted.")
        else:
            print("Aborted.")


if __name__ == "__main__":
    main()
