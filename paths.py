# This file contains all necessary file and folder paths. Make sure to end folder paths with "/".
import os
# basePath is the path from root to the lowest common denominator for all of the other paths.
# Using an absolute path is especially important if running via cron.
basePath = os.getcwd()
# Path to the database file. If you want it somewhere other than directly in the base path you can 
# either write the entire path manually, or just add the rest of the path on top of the basePath.
databasePath = os.path.join(basePath, "db", "database.json")
# Path to backup of database.
backupPath = os.path.join(basePath,"db","database.bak")
# Path for storing logs
logPath = os.path.join(basePath, "logs")
# Path to folder for temporary storage of images
imagePath = os.path.join(basePath, "images")
