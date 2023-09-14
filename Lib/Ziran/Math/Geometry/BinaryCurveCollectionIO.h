#ifndef BINARY_CURVE_COLLECTION_IO_H

#define BINARY_CURVE_COLLECTION_IO_H

#include <Ziran/CS/Util/Forward.h>
#include <string>
namespace ZIRAN {

template <class T, int dim>
void readBinaryCurveCollectionFile(const std::string &filename,
                                   StdVector<Vector<T, dim>> &X,
                                   StdVector<Vector<int, 2>> &segments);
}

#endif
