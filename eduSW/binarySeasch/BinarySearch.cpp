int BinarySearch (int s, int e, int d){
    while (s <= e) {
        int m = (s+e)/2;
        if (A[m] == d) return m;
        else if (A[m] < d) s= m+1; // s~m:X , m+1~e : 가능성
        else e=m-1; // m ~ e : X, s~ m-1 : 가능성
    }
    return -1;
}

int BSLower(int s, int e, int d){
    int sol = -1;
    while (s <= e){
        int m = (s+e) / 2;
        if (A[m] >= d) {
            sol = m;
            e = m-1;
        } else {
            s = m+1;
        }
    }

    return sol;
}

int BSUpper(int s, int e, int d){
    int sol = -1;
    while (s <= e){
        int m = (s+e) / 2;
        if (A[m] <= d) {
            sol = m;
            s = m+1;
        } else {
            e = m-1;
        }
    }

    return sol;
}