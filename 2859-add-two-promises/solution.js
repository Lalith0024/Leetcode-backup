/**
* @param {Promise} promise1
* @param {Promise} promise2
* @return {Promise}
*/
var addTwoPromises = async function(promise1, promise2) {
    return Promise.all([promise1, promise2]).then((values) => {
    const [val1, val2] = values;
        return val1 + val2;
    })
};                         
