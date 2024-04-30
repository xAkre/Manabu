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

/**
 * Attempt to update the completed status of a todo using the api
 *
 * @param {string} uuid - The todo's uuid
 * @param {boolean} status - What status to update to
 * @return {Promise<boolean>} A boolean indicating whether the update was successful
 */
const setCompletedStatus = async (uuid, status) => {
    const url = `/todos/${uuid}/`;

    return await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            status,
        }),
    })
        .then(() => true)
        .catch(() => false);
};

export { deleteTodo, setCompletedStatus };
