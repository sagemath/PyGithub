import github.GithubObject
import github.Issue
import github.NamedUser

class Attachment(github.GithubObject.CompletableGithubObject):
    """
    This class represents Attachments. (Migration archive only.)
    """

    def __repr__(self):
        return self.get__repr__(
            {"asset_name": self._asset_name.value}
        )

    @property
    def asset_content_type(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._asset_content_type)
        return self._asset_content_type.value

    @property
    def asset_name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._asset_name)
        return self._asset_name.value

    @property
    def asset_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._asset_url)
        return self._asset_url.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def issue(self):
        self._completeIfNotSet(self._issue)
        return self._issue.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def user(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._user)
        return self._user.value

    @property
    def _identity(self):
        return self.asset_url

    def _initAttributes(self):
        self._asset_content_type = github.GithubObject.NotSet
        self._asset_name = github.GithubObject.NotSet
        self._asset_url = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._issue = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._user = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "asset_content_type" in attributes:  # pragma no branch
            self._asset_content_type = self._makeStringAttribute(
                attributes["asset_content_type"]
            )
        if "asset_name" in attributes:  # pragma no branch
            self._asset_name = self._makeStringAttribute(
                attributes["asset_name"]
            )
        if "asset_url" in attributes:  # pragma no branch
            self._asset_url = self._makeStringAttribute(
                attributes["asset_url"]
            )
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "issue" in attributes:  # pragma no branch
            self._issue = self._makeClassAttribute(
                github.Issue.Issue, attributes["issue"]
            )
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["user"]
            )
