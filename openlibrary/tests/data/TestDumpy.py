
import json

from openlibrary.data.dump import print_dump, pgdecode

class testDumpy:
#===================================================================

    def test_skip_people_page(self, capsys):
        records = [{"key": "/people/foo"}]
        print_dump(map(json.dumps, records))
        assert capsys.readouterr().out == ""
#====================================================================

    def test_skip_old_page(self, capsys):
        records = [{"key": "/old/what"}]

        print_dump(map(json.dumps, records))
        assert capsys.readouterr().out == ""
#=====================================================================

    def test_skip_wrong_format(self, capsys):
        records = [{"key": "/people//foo"}]


        print_dump(map(json.dumps, records))
        assert capsys.readouterr().out == ""       
#=======================================================================

    def test_skip_spam(self, capsys):
        records = [{"key": "scan/what"}]

        print_dump(map(json.dumps, records))
        assert capsys.readouterr().out == ""
#=====================================================================

    def test_skip_admin_page(self, capsys):
        records = [{"key": "/admin/foo"}]

        print_dump(map(json.dumps, records))
        assert capsys.readouterr().out == ""
#=====================================================================

    def test_noFilter(self, capsys):
        records = [
            {
                "key": "/a/OL1M",
                "type": {"key": "/type/author"},
                "revision": 1,
                "last_modified": {"value": "2019-01-01T00:00:00.000"},
            },
        ]

        print_dump(map(json.dumps, records))
        assert "/authors/OL1M" in capsys.readouterr().out
#=====================================================================

    def test_Filter_match(self, capsys):
        records = [
            {
                "key": "/a/OL1M",
                "type": {"key": "/type/author"},
                "revision": 1,
                "last_modified": {"value": "2019-01-01T00:00:00.000"},
            },
        ]
        
        def test_filter(var):
           return True

        print_dump(map(json.dumps, records), test_filter)
        assert "/authors/OL1M" in capsys.readouterr().out
#=====================================================================

    def test_filter_noMatch(self, capsys):
        records = [{"key": "/admin/foo"}]

        def test_filter(var):
           return False

        print_dump(map(json.dumps, records), test_filter)
        assert capsys.readouterr().out == ""
#=====================================================================



        

   # def test_excludes(self, capsys):
    #    records = [
     #       {"key": "/scan_record/foo"},
      #      {"key": "/old/what"},
       # ]



 #              def test_filter(var):
#            return True


       # print_dump(map(json.dumps, records))
        #assert capsys.readouterr().out == ""  



#    def test_excludes_sensitive_pages(self, capsys):
#        records = [
#            {"key": "/people/foo"},
#            {"key": "/user/foo"},
#            {"key": "/admin/foo"},
#        ]
#        print_dump(map(json.dumps, records))
#        assert capsys.readouterr().out == ""

#    def test_excludes_obsolete_pages(self, capsys):
#        records = [
#            {"key": "/scan_record/foo"},
#            {"key": "/old/what"},
#        ]

#        print_dump(map(json.dumps, records))
#        assert capsys.readouterr().out == ""