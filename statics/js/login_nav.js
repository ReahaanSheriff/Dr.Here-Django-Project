 $('#pat_arrow').removeClass('arrow');
      $('#pills-patient-tab').on('click',function(){
        $('#pat_arrow').addClass('arrow');
        $('#doc_arrow').removeClass('arrow');
       
      });

      $('#pills-doctor-tab').on('click',function(){
        $('#pat_arrow').removeClass('arrow');
        $('#doc_arrow').addClass('arrow');
       
      });

