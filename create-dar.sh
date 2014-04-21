#!/bin/sh

rm -f Intro-1.0.dar Intro-2.0.dar

cd Intro/1.0
jar cvf ../../Intro-1.0.dar *
cd ../..

cd Intro/2.0
jar cvf ../../Intro-2.0.dar *
cd ../..

