import github.GithubObject
import github.NamedUser

class RepositoryFile(github.GithubObject.CompletableGithubObject):
    """
    This class represents RepositoryFiles. (Migration archive only.)
    """

    def __repr__(self):
        return self.get__repr__(
            {"file_name": self._file_name.value}
        )

    @property
    def file_content_type(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._file_content_type)
        return self._file_content_type.value

    @property
    def file_name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._file_name)
        return self._file_name.value

    @property
    def file_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._file_url)
        return self._file_url.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

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
        return self.file_url

    def _initAttributes(self):
        self._file_content_type = github.GithubObject.NotSet
        self._file_name = github.GithubObject.NotSet
        self._file_url = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._user = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "file_content_type" in attributes:  # pragma no branch
            self._file_content_type = self._makeStringAttribute(
                attributes["file_content_type"]
            )
        if "file_name" in attributes:  # pragma no branch
            self._file_name = self._makeStringAttribute(
                attributes["file_name"]
            )
        if "file_url" in attributes:  # pragma no branch
            self._file_url = self._makeStringAttribute(
                attributes["file_url"]
            )
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["user"]
            )
