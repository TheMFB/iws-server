function FeaturesViewModel() {
    var self = this;
    self.featuresURI = 'http://iws-server-dev.us-west-2.elasticbeanstalk.com/v1/features/';
    self.clientsURIBase = 'http://iws-server-dev.us-west-2.elasticbeanstalk.com/v1/features/clients/';
    self.username = "iws";
    self.password = "pass";
    self.features =  ko.observableArray();

    self.clientRoster = ko.observableArray([]);
    this.currentClientArray = ko.observableArray([]);
    this.clientToAdd = ko.observable("");

    this.selectedClientFilter = ko.observable("")
    this.selectedClientFilter.extend({ notify: 'always' });;
    this.selectedClient = ko.observable("");

    this.createTitle = ko.observable("");
    this.createDescription = ko.observable("");
    this.createTargetDate = ko.observable(moment());
    this.createProductArea = ko.observable("");

    this.updateTitle = ""
    this.updateDescription = ""
    this.updateTargetDate = ""
    this.updateProductArea = ""

    this.productAreaArray = ['Policies', 'Billing', 'Claims', 'Reports'];
    this.client_id = "";
    this.feature_id_to_update = "";
    
    var createFeatureModel = {
        selected_client: this.selectedClient(),
        added_client: this.clientToAdd(),
        title: this.createTitle(),
        description: this.createDescription(),
        target_date: this.createTargetDate(),
        product_area: this.createProductArea()
    };

    // Sets Datepicker data 
    $(document).ready(function () {   
        $('.datepicker').datepicker();
    }); 

    self.add_placeholders = function() {
        $(".updateTitle").attr("placeholder", this.updateTitle);
        $(".updateDescription").attr("placeholder", this.updateDescription);
        $(".updateTargetDate").attr("placeholder", this.updateTargetDate);
        $(".updateProductArea").val(this.updateProductArea);
    }

    self.ajax = function(uri, method, data) {
        var request = {
            url: uri,
            type: method,
            contentType: "application/json",
            accepts: "application/json",
            cache: false,
            dataType: 'json',
            data: JSON.stringify(data),
            header: {'Access-Control-Allow-Origin': "*"},
            beforeSend: function (xhr) {
                xhr.setRequestHeader("Authorization",
                    "Basic " + btoa(self.username + ":" + self.password));
            },
            error: function(jqXHR) {
                console.log("ajax:" + jqXHR.status);
            }
        };
        return $.ajax(request);
    }

    this.getFeatures = function() {
        self.ajax(self.featuresURI, 'GET').done(function(data) {
            console.log(data);
            for (let feature of data) {
                self.features.push({
                    id: ko.observable(feature.id),
                    title: ko.observable(feature.title),
                    description: ko.observable(feature.description),
                    client: ko.observable(feature.client),
                    client_priority: ko.observable(feature.client_priority),
                    target_date: ko.observable(feature.target_date),
                    product_area: ko.observable(feature.product_area),
                    editable: ko.computed(function () {
                        return !!((self.selectedClientFilter() || null) && self.selectedClientFilter() == feature.client);
                    })
                });
            }          
        })
    };

    this.getFeatures();

    self.ajax(self.clientsURIBase, 'GET').done(function(data) {
        for (i in data) 
            {self.clientRoster.push(data[i])};
    });

    this.sendRequest = function() {
        data = {
            title: this.createTitle(),
            description: this.createDescription(),
            client: this.selectedClient() || this.clientToAdd(),                
            target_date_month: parseInt(moment(this.createTargetDate(), 'MM/DD/YYYY').format('M')),
            target_date_day: parseInt(moment(this.createTargetDate(), 'MM/DD/YYYY').format('D')),
            target_date_year: parseInt(moment(this.createTargetDate(), 'MM/DD/YYYY').format('YYYY')),
            product_area: this.createProductArea()
        };
        self.ajax(self.featuresURI, 'POST', data);
        location.reload();
        this.getFeatures();
    };

    this.sendUpdateRequest = function(feature_id) {
        data = {
            title: this.updateTitle(),
            description: this.updateDescription(),              
            target_date_month: parseInt(moment(this.updateTargetDate(), 'MM/DD/YYYY').format('M')),
            target_date_day: parseInt(moment(this.updateTargetDate(), 'MM/DD/YYYY').format('D')),
            target_date_year: parseInt(moment(this.updateTargetDate(), 'MM/DD/YYYY').format('YYYY')),
            product_area: this.createProductArea()
        };
        self.ajax(self.featuresURI + feature_id, 'PUT', data);
        location.reload();
        this.getFeatures();
    };

    // Deletes the Feature
    this.sendDelete = function(feature_id) {
        self.ajax(self.featuresURI + feature_id, 'DELETE');
        location.reload();
        this.getFilteredFeatures()
        this.updatePriority();
    }

    //Updates on Priority Changes
    this.updatePriority = function() {
        const features_priorities = [], client_name = $('#clientSelectForm').val();
        if (!client_name) {
            return;
        }
        let features = self.features();
        $('#features_table_editable tbody tr').each(function (indx, tr) {
            let $tr = $(tr), id = $tr.attr('id'), feature = features.filter(function (f) {
                return f.id() === id;
            }) || null;
            if (feature && feature.length > 0) {
                feature[0].client_priority(indx + 1);
            }
            features_priorities.push(id);
        });
        self.ajax(self.clientsURIBase + client_name + '/priority/', 'PUT', features_priorities);
    };

    this.getFilteredFeatures = function () {
        let self = this;
        return ko.computed(function () {
            const client_name = self.selectedClientFilter();
            if (!(client_name || null)) {
                $("#features_table_editable tbody").sortable('disable');
                return self.features();
            }
            $("#features_table_editable tbody").sortable('enable');
            return self.features().filter(function (feature) {
                return feature.client() == client_name;
            }).sort(function (featureA, featureB) {
                return featureA.client_priority() > featureB.client_priority();
            });
        });
    };
};
