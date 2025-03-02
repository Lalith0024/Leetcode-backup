/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if (n === 0) {
        return arr;
    }

    let newarr = [];

    for (let i = 0; i < arr.length; i++) {
        let val = arr[i];

        if (Array.isArray(val)) {
            let flattenedSubArray = flat(val, n - 1);

            for (let j = 0; j < flattenedSubArray.length; j++) {
                newarr.push(flattenedSubArray[j]);
            }
        } else {
            newarr.push(val);
        }
    }
    return newarr;
}
