document.getElementById('commentForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    const commentContent = document.getElementById('commentContent').value;
  
    const requestBody = {
      blog: {
        title: title,
        content: content,
        nb_comments: 0,
        published: true
      },
      content: commentContent
    };
  
    fetch('http://localhost:8000/blog/new/5/comment?commentId=7', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestBody)
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('response').textContent = 'Comment posted successfully!';
      console.log(data);
    })
    .catch(error => {
      document.getElementById('response').textContent = 'An error occurred.';
      console.error('Error:', error);
    });
  });
  