from ..models import Article

class ArticleFlowService:
    def createArticle(self, data):
        newArticle = Article.objects.create(
            title=data['title'],
            body=data['body'],
            status='request'
        )

        return newArticle.id
        

    def chageStatusToAproved(id):
        article = Article.objects.get(id=id)
        article.status = 'aproved'
        article.save()
        return {'status': article.status,'id':id}


    def changeStatusToCancel(id):
        article = Article.objects.get(id=id)
        article.status = 'cancel'
        article.save()
        return {'status': article.status,'id':id}
