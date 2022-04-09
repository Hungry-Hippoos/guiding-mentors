function handleReplyButton(responseId) {
    const replyFormcontainer = document.getElementById(
      `reply-form-container-${responseId}`
    );
    if (replyFormcontainer) {
      replyFormcontainer.className = 'reply-form-container enabled';
    }
  }
  
  function handleCancelReply(responseId) {
    const replyFormcontainer = document.getElementById(
      `reply-form-container-${responseId}`
    );
    if (replyFormcontainer) {
      replyFormcontainer.className = 'reply-form-container';
    }
  }
  