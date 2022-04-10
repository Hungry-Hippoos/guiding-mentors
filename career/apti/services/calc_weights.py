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
    q1_mapping = {"0":"Math",
        "1":"Science",
        "2":"English",
        "3":"Computer science",
        "4":"Accounts",
        "5":"Arts",
        "6":"Other languages",}
    q2_args = {"science":["physics","chemistry","biology","maths"],
               "commerce": ["oc","sp","bk","economics"],
               "arts":["language","political science","sociology", "history"]}
    q2_mapping ={"0":"Math",
        "1":"Physics",
        "2":"Biology",
        "3":"Chemistry",
        "4":"Commerce",
        "5":"Secretarial Practice",
        "6":"Economics",
        "7":"Book Keeping",
        "8":"Organization of Commerce",
        "9":"Computer science",
        "10":"Languages",
        "11":"political Science",
        "12":"Sociology",
        "13":"History",
        "14":"Geography"}
    scores = {"science":0,
              "commerce":0,
              "arts":0}
    weights = get_weights()
    print("Weights",weights)

    for name, answer in responses.items():
        if name =="q1":
            count = {"science": 0,
                      "commerce": 0,
                      "arts": 0}
            for subject in answer:
                if q1_mapping.get(subject) in q1_args.get("science"):
                    count["science"] += 1
                if q1_mapping.get(subject) in q1_args.get("commerce"):
                        count["commerce"] += 1
                if q1_mapping.get(subject) in q1_args.get("arts"):
                    count["arts"] += 1
            for stream,score in scores.items():
                scores[stream] += count[stream]*weights.get("q1")
        if name =="q2":
            count = {"science": 0,
                      "commerce": 0,
                      "arts": 0}
            for subject in answer:
                if q2_mapping.get(subject) in q2_args.get("science"):
                    count["science"] += 1
                if q2_mapping.get(subject) in q2_args.get("commerce"):
                        count["commerce"] += 1
                if q2_mapping.get(subject) in q2_args.get("arts"):
                    count["arts"] += 1
            for stream,score in scores.items():
                scores[stream] += count[stream]*weights.get("q2")
        field = max(zip(scores.values(), scores.keys()))[1]
        return field



def get_weights():
    df = pd.read_csv("cs.csv").iloc[:, 1:]
    normalized = normalize_ratings({"weights":df})
    return normalized



def normalize_ratings(rating):
    means = 0
    weights = {}
    for name,ratings in rating.items():
        means = ratings.mean()
        sd = ratings.std()
        for i in range(len(ratings.columns)):
            ratings.iloc[:,i] = ratings.iloc[:,i].apply(lambda x: (x-means.iloc[i])/sd.iloc[i]).mean()
    print(means.values)
    for i in range(7):
        weights["q"+str(i+1)] = means.values[i]
    print("W",weights)
    return weights