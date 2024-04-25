/**
 * Attempt to delete a todo using the api
 *
 * @param {string} uuid - The todo's uuid
 * @returns {bool} A boolean indicating whether the deletion was successful
 */
const deleteTodo = (uuid) => {
    const url = `/todos/${uuid}/`;

    return fetch(url, {
        method: 'DELETE',
    })
        .then(() => true)
        .catch(() => false);
};

export { deleteTodo };
