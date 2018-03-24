CC = g++
CFLAGS = -g -Wall
SRCS = stitching.cpp
PROG = stitching

OPENCV = `pkg-config opencv --cflags --libs`
LIBS = $(OPENCV)

$(PROG):$(SRCS)
	$(CC) $(CFLAGS) -o $(PROG) $(SRCS) $(LIBS)
