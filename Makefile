LIB_URL = http://www.sogenactif.com/fileadmin/telechargements/sogenactif_p600_C_linux-2.6.9.tar

all: shared-library

shared-library: libsips.so

sogenactif_p600_C_linux-2.6.9.tar:
	wget $(LIB_URL)

libapipayment.a: sogenactif_p600_C_linux-2.6.9.tar
	tar xf sogenactif_p600_C_linux-2.6.9.tar -O lib/libapipayment.a > libapipayment.a

*.o: libapipayment.a
	ar x libapipayment.a

libsips.so: *.o
	gcc -shared -Wl,-soname,libsips.so -o libsips.so *.o

clean:
	rm -f sogenactif_p600_C_linux-2.6.9.tar
	rm -f libapipayment.a
	rm -f *.o
	rm -f libsips.so
