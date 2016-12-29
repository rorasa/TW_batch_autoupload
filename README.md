# TW_batch_autoupload
A python script to create TiddlyWiki's ExternalImage tiddlers to all images in a directory.

This script create a new empty TiddlyWiki called "gallery.html" at the destination folder based on a modified Empty Edition of TiddlyWiki.
A ExternalImage tiddler is created for each image and every image in the destination folder, and included into the newly created wiki.

This script is designed for one-time use only. Once the gallery.html is created, the mark used by TW_batch_autoupload is removed.
The created wiki then becomes a regular TiddlyWiki with no modification.

To use this script, do
```
python autouploader.py <destination>
```
