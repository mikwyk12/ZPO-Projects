#include <iostream>
#include "TSP.hpp"

int main() {
    cost_matrix_t cm = {{INF, 10, 8,   19, 12},
                        {10, INF, 20,  6,  3},
                        {8,   20, INF, 4,  2},
                        {19,  6,  4, INF,  7},
                        {12,  3,  2,   7, INF}};

    CostMatrix temp(cm);

    for (auto elem : temp.get_min_values_in_rows()) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
    std::cout << temp.reduce_rows() << std::endl;

    for (auto elem : temp.get_min_values_in_cols()) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
    std::cout << temp.reduce_cols() << std::endl;

    std::cout << temp.get_vertex_cost(2,2);

    return 0;
}
