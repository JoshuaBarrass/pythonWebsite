function deleteNote(noteId) {
  fetch("/delete-note", {
    //Sends Post request to endpoint /delete-note
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    // when it gets responce
    window.location.href = "/"; // relode page
  });
}
