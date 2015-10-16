# -*- Makefile -*-
#
# Makefile for bsnn
#
# Author: Chase Shyu <chaseshyu@gmail.com>
#
FILE2 = sointerface2
INSTDIR = ./so


########################################################################
## Select default C++ compiler
########################################################################

CPP = gcc

########################################################################
## any customized flags
########################################################################
CFLAGS = -g -Wall -fPIC 
LDFLAGS = -g -Wall -shared
PYFLAGS = 


########################################################################
## default command line options
########################################################################
debug = 0
omp = 0
cache = 1

########################################################################
## Select compiler and linker flags
## (Usually you won't need to modify anything below)
########################################################################

## for no cache .pyc
ifeq ($(cache),0)
	PYFLAGS += -B
endif

## for GNU gcc >= 4.2
ifeq ($(CPP), gcc)
	ifeq ($(omp), 1)
		CFLAGS += -fopenmp
	endif
	ifeq ($(debug), 0)
		CFLAGS += -O3 -ffast-math
	else
		CFLAGS += -O0 -Wall -fbounds-check -ftrapv -fbacktrace -fdump-core \
			-Waliasing -Walign-commons -Wampersand -Wintrinsic-shadow \
			-Wline-truncation -Wsurprising -Wunderflow \
			-finit-integer=-99 -finit-real=nan -frange-check
	endif
endif


########################################################################
## list of source files
########################################################################

SRCS =	\
	sointerface.cpp

SRCS2 =	\
	sointerface2.cpp


OBJS = $(SRCS:.cpp=.o)
OBJS2 = $(SRCS2:.cpp=.o)

EXE = sointerface.so

########################################################################
## actions
########################################################################
#all: $(EXE)

$(EXE): $(OBJS)
	$(CPP) $(LDFLAGS) $(OBJS) -o $@
	@mv $(EXE) $(INSTDIR)

$(OBJS): %.o : %.cpp
	$(CPP) $(CFLAGS) -c $<


test2:$(OBJS2)
	$(CPP) $(LDFLAGS) $(OBJS2) -o $(EXE)
	@mv $(EXE) $(INSTDIR)

$(OBJS2): $(SRCS2)
	$(CPP) $(CFLAGS) -c $<

clean:
	@rm -f $(OBJS) $(OBJS2) $(EXE)

run:
	python3.4 $(PYFLAGS) ./main.py