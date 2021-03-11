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

function deleteCheckItem(checkId) {
  fetch("/delete-check", {
    //Sends Post request to endpoint /delete-note
    method: "POST",
    body: JSON.stringify({ checkId: checkId }),
  }).then((_res) => {
    // when it gets responce
    window.location.href = "/CheckList"; // relode page
  });
}

function changeCheckItemState(checkId) {
  fetch("/change-item-state", {
    //Sends Post request to endpoint /delete-note
    method: "POST",
    body: JSON.stringify({ checkId: checkId }),
  }).then((_res) => {
    // when it gets responce
    window.location.href = "/CheckList"; // relode page
  });
}
