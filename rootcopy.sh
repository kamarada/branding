#!/bin/bash
rm rootcopy.tar.gz

cd rootcopy
tar -zcvf rootcopy.tar.gz *
mv rootcopy.tar.gz ../
cd ..