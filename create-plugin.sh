#!/bin/sh

rm -f intro-plugin-*.jar

cd plugin
jar cvf ../intro-plugin-0.9.jar *
cd ../..
