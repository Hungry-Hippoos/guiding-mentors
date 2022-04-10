function post(path, params, method='post') {

  // The rest of this code assumes you are not using a library.
  // It can be made less verbose if you use one.
  const form = document.createElement('form');
  form.method = method;
  form.action = path;
  for (const key in params) {
    if (params.hasOwnProperty(key)) {
      const hiddenField = document.createElement('input');
      hiddenField.type = 'hidden';
      hiddenField.name = key;
      hiddenField.value = JSON.stringify(params[key]);

      form.appendChild(hiddenField);
    }
  }

  document.body.appendChild(form);
  form.submit();
}

var quiz = {
    // (A) PROPERTIES
    // (A1) QUESTIONS & ANSWERS
    // Q = QUESTION, O = OPTIONS, A = CORRECT ANSWER
    data: [
    {
      q : "Subjects that you liked to study ",
      o : [
        "Math",
        "Science",
        "English",
        "Computer science",
        "Accounts",
        "Arts",
        "Other languages",

      ],
    },
    {
      q : "Subjects you wish to pursue in the future?",
      o : [
        "Math",
        "Physics",
        "Biology",
        "Chemistry",
        "Commerce",
        "Secretarial Practice",
        "Economics",
        "Book Keeping",
        "Organization of Commerce",
        "Computer science",
        "Languages",
        "political Science",
        "Sociology",
        "History",
        "Geography"
      ],
    },
    {
      q : "How do you like to work? ",
      o : [
        "Working in group",
        "Working alone",
        "No Preference"

      ],
    },
    {
      q : "Your dream profession ?",
      o : [
        "Working in group",
        "Working alone",
        "No Preference"
      ],
    },
    {
      q : "Which of the following professions seems interesting to you?",
        o : [
    "software development",
    "supply chain manager",
    "scientist",
    "pilot",
    "chef",
    "author",
    "Journalist",
    "Astronaut",
    "Risk analyst",
    "Psychiatrist",
    "CA",
    "Doctor",
    "Sales Executive",
    "teacher"

      ],
    },
    {
      q : "Your creativity and communication skills",
        o : [
        "1",
        "2",
        "3"
      ],
    },
    {
    q : "Solved an existing problem for anyone on any scale",
        o : [
        "Yes",
        "No",
      ],
     }
    ],
    ans:{
      0:{
        opt:3,
        ans:[]
      },
      1:{
        opt:3,
        ans:[]
      },
      2:{
        opt:1,
        ans:[]
      },
      3:{
        opt:1,
        ans:[]
      },
      4:{
        opt:3,
        ans:[]
      },
      5:{
        opt:1,
        ans:[]
      },
      6:{
        opt:1,
        ans:[]
      }
    },
    // (A2) HTML ELEMENTS
    hWrap: null, // HTML quiz container
    hQn: null, // HTML question wrapper
    hAns: null, // HTML answers wrapper
  
    // (A3) GAME FLAGS
    now: 0, // current question
    score: 0, // current score
  
    // (B) INIT QUIZ HTML
    init: () => {
      // (B1) WRAPPER
      quiz.hWrap = document.getElementById("quizWrap");
  
      // (B2) QUESTIONS SECTION
      quiz.hQn = document.createElement("div");
      quiz.hQn.id = "quizQn";
      quiz.hWrap.appendChild(quiz.hQn);
  
      // (B3) ANSWERS SECTION
      quiz.hAns = document.createElement("div");
      quiz.hAns.id = "quizAns";
      quiz.hWrap.appendChild(quiz.hAns);
  
      // (B4) GO!
      quiz.draw();
    },
  
    // (C) DRAW QUESTION
    draw: () => {
      // (C1) QUESTION
      quiz.hQn.innerHTML = quiz.data[quiz.now].q;
  
      // (C2) OPTIONS
      quiz.hAns.innerHTML = "";
      for (let i in quiz.data[quiz.now].o) {
        let radio = document.createElement("input");
        radio.type = "radio";
        radio.name = "quiz";
        radio.id = "quizo" + i;
        quiz.hAns.appendChild(radio);
        let label = document.createElement("label");
        label.innerHTML = quiz.data[quiz.now].o[i];
        label.setAttribute("for", "quizo" + i);
        label.dataset.idx = i;
        label.addEventListener("click", () => { quiz.select(label); });
        quiz.hAns.appendChild(label);
      }
    },
  
    // (D) OPTION SELECTED
    select: (option) => {
      // (D1) DETACH ALL ONCLICK
      // let all = quiz.hAns.getElementsByTagName("label");
      // for (let label of all) {
      //   label.removeEventListener("click", quiz.select);
      // }
  
      // (D2) CHECK IF CORRECT
      console.log(option.dataset.idx)
      // (D3) NEXT QUESTION OR END GAME
      if((quiz.ans[quiz.now].opt-1)!=0){
        quiz.ans[quiz.now].opt--;
        quiz.ans[quiz.now].ans.push(option.dataset.idx);
      }else{
        console.log(quiz.ans[quiz.now].ans);
        quiz.ans[quiz.now].ans.push(option.dataset.idx);
        quiz.now++;
      }
      setTimeout(() => {
        if (quiz.now < quiz.data.length) { quiz.draw(); }
        else {
          for(i=0;i<quiz.ans.length;i++){
            quiz.ans[i]=quiz.ans[i].ans;
          }
          console.log(JSON.stringify(quiz.ans));
          // axios({
          //   method: 'post',
          //   url: '/quiz/',
          //   data: JSON.stringify(quiz.ans)
          // });
          post('/quiz/', quiz.ans)

        }
      }, 100);
    },
  
    // (E) RESTART QUIZ
    reset : () => {
      quiz.now = 0;
      quiz.score = 0;
      quiz.ans={
        0:{
          opt:3,
          ans:[]
        },
        1:{
          opt:3,
          ans:[]
        },
        2:{
          opt:1,
          ans:[]
        },
        3:{
          opt:1,
          ans:[]
        },
        4:{
          opt:3,
          ans:[]
        },
        5:{
          opt:1,
          ans:[]
        },
        6:{
          opt:1,
          ans:[]
        }
      };
      quiz.draw();
    }
  };
  window.addEventListener("load", quiz.init);
