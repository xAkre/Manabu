/**
 * Attempt to delete a category using the api
 *
 * @param {string} uuid - The category's uuid
 * @returns {bool} A boolean indicating whether the deletion was successful
 */
const deleteCategory = (uuid) => {
    const url = `/categories/${uuid}/`;

    return fetch(url, {
        method: 'DELETE',
    })
        .then(() => true)
        .catch(() => false);
};

export { deleteCategory };
