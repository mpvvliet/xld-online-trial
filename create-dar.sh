#!/bin/sh

cd Intro/1.0
jar cvfm ../../Intro-1.0.dar META-INF/MANIFEST.MF *
cd ../..

cd Intro/2.0
jar cvfm ../../Intro-2.0.dar META-INF/MANIFEST.MF *
cd ../..

