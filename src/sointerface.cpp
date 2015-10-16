//
//  sointerface.cpp
//  
//
//  Created by Phoenix on 10/15/15.
//
//
#define SOEXPORT extern "C" __declspec()

SOEXPORT int sum(int a, int b) {
    return a + b;
}
