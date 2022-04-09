import pandas as pd


def generate_field(responses):
    '''
    responses = {"q1": ["math","science", "history"],
    "
    :param responses:
    :return:
    '''
    q1_args = {"science":["english","maths","science"],
               "commerce": ["english","maths"],
               "arts":["english","other_lang","social studies"]}
    q2_args = {"science":["physics","chemistry","biology","maths"],
               "commerce": ["oc","sp","bk","economics"],
               "arts":["language","political science","sociology", "history"]}
    scores = {"science":0,
              "commerce":0,
              "arts":0}
    weights = get_weights()
    for name, answer in responses.items():
        if name =="q1":
            count = {"science": 0,
                      "commerce": 0,
                      "arts": 0}
            for subject in answer:
                if subject in q1_args.get("science"):
                    count["science"] += 1
                if subject in q1_args.get("commerce"):
                        count["commerce"] += 1
                if subject in q1_args.get("arts"):
                    count["arts"] += 1
            for stream,score in scores.items():
                scores[stream] += count[stream]*weights.get("q1")
        if name =="q2":
            count = {"science": 0,
                      "commerce": 0,
                      "arts": 0}
            for subject in answer:
                if subject in q2_args.get("science"):
                    count["science"] += 1
                if subject in q2_args.get("commerce"):
                        count["commerce"] += 1
                if subject in q2_args.get("arts"):
                    count["arts"] += 1
            for stream,score in scores.items():
                scores[stream] += count[stream]*weights.get("q2")
        field = max(zip(scores.values(), scores.keys()))[1]



def get_weights():
    df = pd.read_csv("career\cs.csv").iloc[:, 1:]
    normalized = normalize_ratings({"weights":df})
    q1_args = {"science":["english","maths","science"],
               "commerce": ["english","maths"],
               "arts":["english","other_lang","social studies"]}



def normalize_ratings(rating):
    for name,ratings in rating.items():
        means = ratings.mean()
        sd = ratings.std()
        for i in range(len(ratings.columns)):
            ratings.iloc[:,i] = ratings.iloc[:,i].apply(lambda x: (x-means.iloc[i])/sd.iloc[i])
    print(rating)
    return rating