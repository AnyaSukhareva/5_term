IP: 192.168.100.101 
ssh port: 22

user:
mpiuser

passwrd:
8A3ps#374C33



servername: ubuntu-srv01
---------------------------------------------

Compile openmp:
gcc -O2 -o omp_hello -fopenmp omp_hello.c -lm

run:
./omp_hello

or 

gcc -O2 -o integrate -fopenmp omp_integrate.c -lm

run:
./integrate


run:
./omp_hello

set number of threads:
export OMP_NUM_THREADS=3

---------------------------------------------

Compile mpi:
mpicc ./mpi_pi.c -o ./pi

run:
mpiexec -hostfile mpi.host -n 5 ./pi

