import json
import urllib2

# Fuck you python.
# If someone can explain to me why python makes this such a
# pain In the ass I would love that
try:
    from travis.gitrepo import GitRepo
    from travis.travisresponse import TravisResponse
except ImportError:
    from gitrepo import GitRepo
    from travisresponse import TravisResponse


try:
    import vim
except ImportError:
    # Hack to ignore Vim code when running outside of vim
    class vim(object):
        vars = {}


# def main(branch, remote):
def main():
    try:
        repo = GitRepo()
    except ValueError as e:
        print(e)
        return

    url = repo.travis_branch_url(None, None)
    req = urllib2.Request(url,
                          headers={"Accept":
                                   "application/vnd.travis-ci.2+json"})
    try:
        res = urllib2.urlopen(req)
    except (urllib2.HTTPError) as e:
        print("An error occurred: %d - %s" % (e.getcode(), e.reason))
        return

    travis = TravisResponse(json.loads(res.read()), None, repo)
    print(travis.message())


if __name__ == "__main__":
    # main(None, None)
    main()
