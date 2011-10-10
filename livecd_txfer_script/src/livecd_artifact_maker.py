#!/usr/bin/env python
'''
Created on Aug 29, 2011

@author: jds
'''
import os
import sys
import shutil
import tarfile


def remove_stuff(dst_dir, additional_dir):
    if os.path.isdir(dst_dir + additional_dir):
        print "Info: Removing [%s%s]" % ( dst_dir, additional_dir )
        shutil.rmtree(dst_dir + additional_dir) 

if __name__ == '__main__':
    #src_dir = os.path.abspath(os.path.curdir) + "/livecd_builder_trunk"    
    src_dir = os.path.curdir + "/livecd_builder_trunk"    
    dst_dir = src_dir + "_bak"
    if not os.path.exists(src_dir):
        print "Error: %s does not appear to be a valid path" % ( src_dir )
        sys.exit(1)
    
    
    # First copy up all of the stuff.
    #print os.path.basename(dst_dir)
    if os.path.isdir(dst_dir):
        if os.path.dirname(dst_dir) == '/':
            print "Error: Eh? you are trying to delete the entire file system, surley that is not what you intended"        
            sys.exit(1)
        print "Warning: Removing the destionation dir [%s]" % ( dst_dir )
        shutil.rmtree(dst_dir)
        
    

    print "Info: Creating [%s]" % ( dst_dir )
    shutil.copytree(src_dir, dst_dir, symlinks=True)

    # A bit of dir cleanup after the copy....
    remove_stuff(dst_dir, "/.metadata")
    remove_stuff(dst_dir, "/src/anaconda-git-10.1.1.104.loader2/")
    remove_stuff(dst_dir, "/src/anaconda-runtime-10.1.1.103-1-CentOS4")
    remove_stuff(dst_dir, "/src/usr/share/ultra-livecd-tools/replace_files")
    
    tarball=dst_dir + ".tar.gz"
    print "zip... it n rip it.. creatiing tarball [%s]" % (tarball)
    tar = tarfile.open(tarball, "w:gz")
    tar.add(dst_dir)
    tar.close()
    