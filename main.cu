#include <stdio.h>

__global__ void foo()
{
    if (blockIdx.x == 0 && threadIdx.x == 0)
    {
        printf("Kernel running. All good :)\n");
    }
}

int main()
{
    // <<<numBlocks, threadsPerBlock, sizeOfSharedMemory, cudaStream>>>
    foo<<<1, 1>>>();
    cudaDeviceSynchronize();
    return 0;
}