CC = g++
CFLAGS = -g -Wall
SRCS = videostab.cpp
PROG = videostab

OPENCV = `pkg-config opencv --cflags --libs`
LIBS = $(OPENCV)

$(PROG):$(SRCS)
	$(CC) $(CFLAGS) -o $(PROG) $(SRCS) $(LIBS)
