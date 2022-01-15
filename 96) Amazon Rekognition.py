import boto3
import json

def recognize_celebrities(photo):

    f = open ('config.json', 'r')
    key = json.load(f)

    usuario = key['senhas'][1]['user']
    senha = key['senhas'][1]['pass']

    client = boto3.client(
    service_name = 'rekognition',
    region_name = 'us-west-1',
    aws_access_key_id = usuario,
    aws_secret_access_key = senha
    )
    
    with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image={"Bytes": image.read()})
    
    for celebrity in response["CelebrityFaces"]:
        print(f"\nNome: {celebrity['Name']}")
        print(f"Id: {celebrity['Id']}")
        print("Posição:")
        print(f"Left: {celebrity['Face']['BoundingBox']['Height']:.2f}")
        print(f"Top: {celebrity['Face']['BoundingBox']['Top']:.2f}")
        print("Info:")
        for url in celebrity['Urls']:
            print(url)
    return len(response['CelebrityFaces'])


def main():    
    photo = r"C:/Users/50s/Desktop/oscria.jpg"
    #input("Digite o local da imagem: ")
    celeb_count = recognize_celebrities(photo)
    print("\nCelebridades detectadas: " + str(celeb_count))


if __name__ == "__main__":
    main()