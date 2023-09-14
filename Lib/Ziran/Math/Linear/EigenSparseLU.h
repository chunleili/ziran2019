#include <Eigen/SparseCore>
#include <Ziran/CS/Util/Forward.h>

namespace ZIRAN {

template <class T>
void eigenSparseLUSolve(const Eigen::SparseMatrix<T, Eigen::RowMajor> &mat,
                        Eigen::Map<const Vector<T, Eigen::Dynamic>> rhs,
                        Eigen::Map<Vector<T, Eigen::Dynamic>> to_solve);
}
