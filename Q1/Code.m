for i=0:50
    for j=0
        sys = tfest(frdata,i,j);
        MSE_0(i+1,j+1) = sys.Report.Fit.MSE;
        FitPer_0(i+1,j+1) = sys.Report.Fit.FitPercent;
    end
end
